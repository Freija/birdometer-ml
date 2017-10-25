# Freija Descamps 09-2017
# Code to handscan and label birdometer images

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from os import listdir
from os.path import isfile, join
import csv


def main():
    # Grab all the pictures that have already been processed so far
    current_list = []
    with open('../trainingdata/images.handscan.csv', 'r') as infile:
        reader = csv.reader(infile)
        for row in reader:
            current_list.append(row[0])
    # Loop over all the pictures in the directory
    images = [f for f in listdir('../trainingdata/') if isfile(join('../trainingdata/', f)) if f.endswith('.jpg')]
    print(len(images))
    total = len(images)
    counter = 0
    for image in images:
        print(counter, total)
        counter = counter + 1
        if image in current_list:
            print('Skipping')
            continue
        print("Now analyzing ", join('../trainingdata/', image))
        imgplot = plt.imshow(mpimg.imread(join('../trainingdata/', image)))
        plt.ion()
        plt.show()
        bird_present = 'n'
        bird_drinking = 'n'
        correct = 'n'
        while correct != 'y':
            bird_present = input("Is there a bird? (y/n) ")
            if bird_present == 'y':
                bird_drinking = input("Is the bird drinking? (y/n) ")
            print("Answer is ", bird_present, bird_drinking)
            correct = input("Keep answer? ")
        plt.close()
        # Save this information to the file
        with open(r'../trainingdata/images.handscan.csv', 'a') as outf:
            writer = csv.writer(outf)
            writer.writerow((image, bird_present, bird_drinking))


if __name__ == "__main__":
    main()
