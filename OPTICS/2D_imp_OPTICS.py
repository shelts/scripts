#! /usr/bin/python

import os
import subprocess
from subprocess import call
import matplotlib.pyplot as plt
import math as mt
import matplotlib.patches as mpatches
import random
random.seed(a = 123456789)

vgsr_cutoff = 25 
dist_cutoff = 5
l_cutoff    = mt.radians(5)
b_cutoff    = mt.radians(2.5)
min_cluster_size = 10
threshold = 2


#since charles and keighly all have different data
v_column = 24
d_column = 18
l_column = 5
b_column = 6
starts_with = 'g0'
################################################################################
# POINT
################################################################################

class Point:
    
    def __init__(self, l, b):
        
        self.l    = l 
        self.b    = b
        self.cd = None              # core distance
        self.rd = None              # reachability distance
        self.processed = False      # has this point been processed?
        
    # --------------------------------------------------------------------------
    # calculate the distance between any two points in data
    # --------------------------------------------------------------------------
    
    def distance(self, point):
        #self.del_l
        #self.del_b
        #distance is simply the dist between two points in x, y
        #del_vgsrsq =  ( (self.vgsr - point.vgsr)**2 ) 
        #del_distsq =  ( (self.dist - point.dist)**2 ) 
        
        
    # ------------------------------------------------------------------------------
    # KEIG- I need you to put in the distance between two l and b points in the sky
    # ------------------------------------------------------------------------------
        l1_rad = mt.radians(self.l)
        l2_rad = mt.radians(point.l)
        
        b1_rad = mt.radians(self.b)
        b2_rad = mt.radians(point.b)
        
        #angular_dist = ( l1_rad * mt.cos(b1_rad) - l2_rad * mt.cos(b2_rad) )**2 
        angular_dist =  ( (l1_rad - l2_rad)**2  + (b1_rad - b2_rad)**2) 
        
        r = (angular_dist)
        r = mt.sqrt(r)
        
        return r


################################################################################
# CLUSTER
################################################################################

class Cluster:
    
    def __init__(self, points):
        
        self.points = points
        
    # --------------------------------------------------------------------------
    # calculate the centroid for the cluster
    # --------------------------------------------------------------------------

    def centroid(self):
        n_points = len(self.points)
        sum_ls   = sum([p.l    for p in self.points]) / n_points
        sum_bs   = sum([p.b    for p in self.points]) / n_points
        return Point(sum_ls, sum_bs)
            
    # --------------------------------------------------------------------------
    # calculate the region (centroid, bounding radius) for the cluster
    # --------------------------------------------------------------------------
    
    def region(self):
        
        centroid = self.centroid()
        radius = reduce(lambda r, p: max(r, p.distance(centroid)), self.points)
        return centroid, radius
        




        
################################################################################
# OPTICS
################################################################################

class Optics:
    
    def __init__(self, points, max_radius, min_cluster_size):
        
        self.points = points
        self.max_radius = max_radius                # maximum radius to consider
        self.min_cluster_size = min_cluster_size    # minimum points in cluster
    
    # --------------------------------------------------------------------------
    # get ready for a clustering run
    # --------------------------------------------------------------------------
    
    def _setup(self):
        
        for p in self.points:
            p.rd = None
            p.processed = False
        self.unprocessed = [p for p in self.points]
        self.ordered = []

    # --------------------------------------------------------------------------
    # distance from a point to its nth neighbor (n = min_cluser_size)
    # --------------------------------------------------------------------------
    
    def _core_distance(self, point, neighbors):

        if point.cd is not None: return point.cd
        if len(neighbors) >= self.min_cluster_size - 1:
            sorted_neighbors = sorted([n.distance(point) for n in neighbors])
            point.cd = sorted_neighbors[self.min_cluster_size - 2]
            return point.cd
        
    # --------------------------------------------------------------------------
    # neighbors for a point within max_radius
    # --------------------------------------------------------------------------
    
    def _neighbors(self, point):
        
        return [p for p in self.points if p is not point and
            p.distance(point) <= self.max_radius]
            
    # --------------------------------------------------------------------------
    # mark a point as processed
    # --------------------------------------------------------------------------
        
    def _processed(self, point):
    
        point.processed = True
        self.unprocessed.remove(point)
        self.ordered.append(point)
    
    # --------------------------------------------------------------------------
    # update seeds if a smaller reachability distance is found
    # --------------------------------------------------------------------------

    def _update(self, neighbors, point, seeds):
        
        # for each of point's unprocessed neighbors n...

        for n in [n for n in neighbors if not n.processed]:
            
            # find new reachability distance new_rd
            # if rd is null, keep new_rd and add n to the seed list
            # otherwise if new_rd < old rd, update rd
            
            new_rd = max(point.cd, point.distance(n))
            if n.rd is None:
                n.rd = new_rd
                seeds.append(n)
            elif new_rd < n.rd:
                n.rd = new_rd
    
    # --------------------------------------------------------------------------
    # run the OPTICS algorithm
    # --------------------------------------------------------------------------

    def run(self):
        
        self._setup()
        
        # for each unprocessed point (p)...
        
        while self.unprocessed:
            point = self.unprocessed[0]
            
            # mark p as processed
            # find p's neighbors
            
            self._processed(point)
            point_neighbors = self._neighbors(point)

            # if p has a core_distance, i.e has min_cluster_size - 1 neighbors

            if self._core_distance(point, point_neighbors) is not None:
                
                # update reachability_distance for each unprocessed neighbor
                
                seeds = []
                self._update(point_neighbors, point, seeds)
                
                # as long as we have unprocessed neighbors...
                
                while(seeds):
                    
                    # find the neighbor n with smallest reachability distance
                    
                    seeds.sort(key=lambda n: n.rd)
                    n = seeds.pop(0)
                    
                    # mark n as processed
                    # find n's neighbors
                    
                    self._processed(n)
                    n_neighbors = self._neighbors(n)
                    
                    # if p has a core_distance...
                    
                    if self._core_distance(n, n_neighbors) is not None:
                        
                        # update reachability_distance for each of n's neighbors
                        
                        self._update(n_neighbors, n, seeds)
                        
        # when all points have been processed
        # return the ordered list

        return self.ordered
        
    # --------------------------------------------------------------------------
    
    def cluster(self, cluster_threshold):
        
        clusters = []
        separators = []

        for i in range(len(self.ordered)):
            this_i = i
            next_i = i + 1
            this_p = self.ordered[i]
            this_rd = this_p.rd if this_p.rd else float('infinity')
            
            # use an upper limit to separate the clusters
            
            if this_rd > cluster_threshold:
                separators.append(this_i)

        separators.append(len(self.ordered))

        for i in range(len(separators) - 1):
            start = separators[i]
            end = separators[i + 1]
            if end - start >= self.min_cluster_size:
                clusters.append(Cluster(self.ordered[start:end]))

        return clusters





################################################################################
# Main
################################################################################




def get_data(file_name):
    f = open(file_name, 'r')
    vgsr = []
    dist = []
    ls = []
    bs = []
    for line in f:
        if(line.startswith(starts_with)):
               continue
        cols = line.split(',')
        v = float(cols[v_column])
        d = float(cols[d_column])
        l = float(cols[l_column])
        b = float(cols[b_column])
        vgsr.append(v)
        dist.append(d)
        ls.append(l)
        bs.append(b)
        
    return vgsr, dist, ls, bs


def plot_raw_data(d, v):
    plt.ylabel('Vgsr')
    plt.xlabel('distance')
    plt.scatter(d, v, color = 'k', s=0.5, marker='o')
    plt.show()


def plot_raw_data_and_clusters(x, y, cluster_x, cluster_y, counter, name, xlabel, ylabel):
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.scatter(x, y, color = 'k', s=0.5, marker='o')
    for i in range(0 , counter):
        plt.scatter(cluster_x[i], cluster_y[i], s=2, marker='^', alpha=0.50)
    #plt.show()
    plt.savefig(name, format='png', dpi=1000)
    plt.clf()

def make_points( ls, bs):
    points = []
    for i in range(0,len(ls)):
        points.append(Point(ls[i], bs[i]))
    return points


def make_random_points_with_cluster():
    xs = [] 
    ys = []
    N = 370
    y_range = 600
    x_range = 60
    N_cluster = 10
    for i in range(0, N):
        randomx = random.uniform(0.0, 1.0) * x_range
        randomy = random.uniform(-1.0, 1.0) * y_range
        xs.append(randomx)
        ys.append(randomy)
        
    for i in range(0, N_cluster):
        randomx = random.uniform(0.4, 0.5) * x_range
        randomy = random.uniform(0.0, 0.1) * y_range
        xs.append(randomx)
        ys.append(randomy)
    
    for i in range(0, N_cluster):
        randomx = random.uniform(0.45, 0.55) * x_range
        randomy = random.uniform(0.05, 0.15) * y_range
        xs.append(randomx)
        ys.append(randomy)
    
    for i in range(0, N_cluster):
        randomx = random.uniform(0.5, 0.6) * x_range
        randomy = random.uniform(0.1, 0.2) * y_range
        xs.append(randomx)
        ys.append(randomy)
    
    return xs, ys






def find_clusters_lb(points, ls, bs):
    cut_off_rad = mt.sqrt( (l_cutoff * mt.cos(b_cutoff) )**2)
    
    
    optics = Optics(points, cut_off_rad, min_cluster_size) # 100m radius for neighbor consideration, cluster size >= 2 points
    optics.run()                    # run the algorithm
    clusters = optics.cluster(threshold)   # 50m threshold for clustering

    counter = 0
    for cluster in clusters:
        counter += 1

    print counter
    cluster_ls = []
    cluster_bs = []
    
    cluster_ls_tmp = []
    cluster_bs_tmp = []
    
    for cluster in clusters:
        cluster_ls_tmp = []
        cluster_bs_tmp = []
        for i in range(0, len(cluster.points)):
            cluster_ls_tmp.append(cluster.points[i].l)
            cluster_bs_tmp.append(cluster.points[i].b)
        print len(cluster_ls_tmp) , len(cluster_bs_tmp)
        
        cluster_ls.append(cluster_ls_tmp)
        cluster_bs.append(cluster_bs_tmp)
    plot_raw_data_and_clusters(ls   , bs   , cluster_ls   , cluster_bs, counter  , 'l_b'      , 'l'   , 'b')


def find_clusters_vd(points, vgsrs, dists ):
    cut_off_rad = mt.sqrt( vgsr_cutoff**2 + dist_cutoff**2 ) 
    
    
    optics = Optics(points, cut_off_rad, min_cluster_size) # 100m radius for neighbor consideration, cluster size >= 2 points
    optics.run()                    # run the algorithm
    clusters = optics.cluster(threshold)   # 50m threshold for clustering

    counter = 0
    for cluster in clusters:
        counter += 1

    print counter
    cluster_vgrs = []
    cluster_dists = []
    
    
    cluster_vgrs_tmp = []
    cluster_dists_tmp = []
    
    for cluster in clusters:
        cluster_vgrs_tmp = []
        cluster_dists_tmp = []
        for i in range(0, len(cluster.points)):
            cluster_vgrs_tmp.append(cluster.points[i].l)
            cluster_dists_tmp.append(cluster.points[i].b)

        print len(cluster_vgrs_tmp) , len(cluster_dists_tmp)
        
        cluster_vgrs.append(cluster_vgrs_tmp)
        cluster_dists.append(cluster_dists_tmp)
    plot_raw_data_and_clusters(dists, vgsrs, cluster_dists, cluster_vgrs, counter, 'dist_vgsr', 'dist', 'Vgsr' )







def main():
    file_name = "Low_Met.csv"

    vgsrs, dists, ls, bs = get_data(file_name)
    #plot_raw_data(dists, vgsrs)
    
    points_lb = make_points( ls, bs)
    points_vd = make_points( vgsrs, dists)
    
    find_clusters_lb(points_lb, ls, bs)
    
    find_clusters_vd(points_vd, vgsrs, dists)
    
    
    
    # testing with random data #
    #dists, vgsrs = make_random_points_with_cluster()
    #plot_raw_data(dists,vgsrs)
    #points = make_points(vgsrs, dists)
    
    
main()