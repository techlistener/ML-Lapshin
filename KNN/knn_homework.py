import matplotlib.pyplot as plt
import numpy as np
import random

colors = ['black', 'b', 'g', 'r', 'y', 'k', 'w', 'm']


def get_distance(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def plot(x, y, color_index):
    plt.scatter(x, y, c=colors[color_index])


def generate_data_with_classification(number_of_class_el, number_of_classes):
    data = []
    for classNum in range(number_of_classes):
        centerX, centerY = random.random() * 5.0, random.random() * 5.0
        for rowNum in range(int(number_of_class_el)):
            data.append([[random.gauss(centerX, 0.5), random.gauss(centerY, 0.5)], classNum])
    return data


def generate_data_without_classification(number_of_class_el, number_of_classes):
    data = []
    for classNum in range(number_of_classes):
        centerX, centerY = random.random() * 5.0, random.random() * 5.0
        for rowNum in range(int(number_of_class_el)):
            data.append([random.gauss(centerX, 0.5), random.gauss(centerY, 0.5)])
    return data


def knn(k, clusters, classified_objects, objects_that_must_be_classified):
    for i in range(len(classified_objects)):
        color = classified_objects[i][1] + 1
        plot(classified_objects[i][0][0], classified_objects[i][0][1], color)

    plt.show()

    for i in range(len(objects_that_must_be_classified)):
        plot(objects_that_must_be_classified[i][0], objects_that_must_be_classified[i][1], 0)

    plt.show()

    for i in range(len(objects_that_must_be_classified)):
        neighbours = []
        for j in range(len(classified_objects)):
            distance_to_point = get_distance(objects_that_must_be_classified[i][0],
                                             objects_that_must_be_classified[i][1],
                                             classified_objects[j][0][0],
                                             classified_objects[j][0][1])
            point_cluster_number = classified_objects[j][1]
            neighbours.append([distance_to_point, point_cluster_number])
        neighbours.sort()
        k_nearest_neighbours = [neighbours[i] for i in range(k)]

        clusters_c = np.zeros(cl)
        for j in range(len(k_nearest_neighbours)):
            clusters_c[k_nearest_neighbours[j][1]] += 1

        max_neighbours = 0
        cluster_with_max_neighbours = 0

        iterator = 0
        for neighbours_in_cluster in clusters_c:
            if neighbours_in_cluster > max_neighbours:
                max_neighbours = neighbours_in_cluster
                cluster_with_max_neighbours = iterator
            iterator = iterator + 1
        clusters.append(cluster_with_max_neighbours)

    for i in range(len(objects_that_must_be_classified)):
        color = clusters[i] + 1
        plot(objects_that_must_be_classified[i][0], objects_that_must_be_classified[i][1], color)

    plt.show()

k = 20
clusters = []
cl = 4
count_all_objects = cl * 400
count_classified_objects = count_all_objects * 0.8
count_unclassified_objects = count_all_objects * 0.2
classified_objects = generate_data_with_classification(count_classified_objects / cl, cl)
objects_that_must_be_classified = generate_data_without_classification(count_unclassified_objects / cl, cl)

knn(k, clusters, classified_objects, objects_that_must_be_classified)
