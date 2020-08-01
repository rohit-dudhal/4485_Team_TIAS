# -*- coding: utf-8 -*-
#
from Augmentor import Pipeline,Operations

#supply input file path ,output file path ,output
def datasetmaker(filename):
    p = Pipeline(f'C:/Users/DRD PC/Desktop/Image/{filename}',f'C:/Users/DRD PC/Desktop/Image/{filename}')
    p.rotate(probability=0.3, max_left_rotation=15, max_right_rotation=15)
    p.zoom(probability=0.3, min_factor=1.1, max_factor=1.5)
    p.flip_left_right(0.2)
    p.skew_left_right(0.2,0.2)
    p.skew_corner(0.3,0.2)
    p.skew_tilt(0.2,0.2)
    Operations.Greyscale(0.2)
    Operations.BlackAndWhite(0.2,0.2)
    p.random_distortion(0.2, 2, 2, 2)
    p.process()
    p.sample(100)

# Provide file Name
# datasetmaker('Dhyeya')
# datasetmaker('Mayuresh')
# datasetmaker('Raj')
# datasetmaker('Priyanka')
# datasetmaker('Rohit')
# datasetmaker('Tejas')

