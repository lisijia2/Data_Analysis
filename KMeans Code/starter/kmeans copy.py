from pickle import TRUE
import numpy as np
from scipy.spatial import distance

def should_continue(sse_diff, thresh):
    """
    Returns true if we should continue to move our
    centroids.
    
    Args:
        sse_diff  the difference between two consecutive
                  rounds of moving the centroids
        thresh    the change in SSE around zero that
                  indicates a stopping condition
    """
    if sse_diff > thresh:
        return(TRUE)


def get_sse(obs, centroids, labels):
    """
    Finds the sum of the square error (distance) between
    centroids and its labeled observations
    """
    labeled_cent = centroids[labels]
    sse=np.sum((obs-labeled_cent)**2)
    return(sse)


def find_labels(obs, centroids):
    """
    Labels each observation in df based upon
    the nearest centroid. 
    
    Args:
        obs  numpy array of n observations with m dimensions
        centroids numpy array of k centroids with m dimensions
    
    Returns:
        a numpy array of labels, one for each observation
    """
    pw_dist = distance.cdist(obs, centroids)
    labels = np.argmin(pw_dist, axis=1)   # find the min value for each row
    return(labels)



    
def recompute_centroids(obs, centroids, labels):
    """
    Find the new location of the centroids by
    finding the mean location of all points assigned
    to each centroid
    
    Arguments:
        obs  numpy array of observations with n observations in m dimensions
        centroids  k centroids of m dimensions
        labels  n labels; one for each observation
    
    Returns:
        numpy array of k centroids with m dimensions (updated)
    """
    centroids=centroids.astype(np.float32)
    for i in range(len(centroids)):  # len(centroids) = K
        clust = obs[labels==i]
        new_centroid=clust.mean(axis=0)
        centroids[i] = new_centroid
    return(centroids)
        

    
    
def cluster_kmeans(obs, k):
    """
    Clusters the n observations of m attributes 
    
    Euclidean distance is used as the proximity metric.
    
    Arguments:
        obs   numpy array of n observations of m dimensions
        k    the number of clusters to search for
        
    Returns:
        a n-sized numpy array of the cluster labels
        
        the final Sum-of-Error-Squared (SSE) from the clustering

        a k x m numpy array of the centroid locations
    """
    centroids=obs[:k]
    labels=find_labels(obs, centroids)

    sse_list=[] #a list which contains all sse
    sse=get_sse(obs, centroids, labels)
    sse_list.append(sse)

    new_centroids=recompute_centroids(obs, centroids, labels)
    new_labels=find_labels(obs, new_centroids)
    sse=get_sse(obs, new_centroids, new_labels)
    sse_list.append(sse)

    sse_diff=sse_list[-2]-sse_list[-1]
    thresh=0

    while should_continue(sse_diff, thresh):
        new_centroids=recompute_centroids(obs, new_centroids, new_labels)
        new_labels=find_labels(obs, new_centroids)
        sse=get_sse(obs, new_centroids, new_labels)
        sse_list.append(sse)
        sse_diff=sse_list[-2]-sse_list[-1]
    else:
        return new_labels, sse, new_centroids
