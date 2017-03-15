from __future__ import division
import numpy as np
import cv2

class Environment_np:
    def __init__(self, dims):
        self.dims = dims
        self.background_value = 200
        self.visualisation = np.ones((self.dims[0], self.dims[1]), np.float32) * self.background_value
        self.features = []

    def add_feature(self, feature):
        if isinstance(feature, (list,tuple)):
            assert not isinstance(feature, str)
            for f in feature:
                self.features.append(f)
        else:
            self.features.append(feature)

    def get_matrix(self, t):
        for feature in self.features:
            self.visualisation[feature.pos[0]:(feature.pos[0] + feature.dims[0]),
                                feature.pos[1]:(feature.pos[1] + feature.dims[1])] = feature.make_waves(t)
        return self.visualisation


    def draw(self, t):
        self.visualisation = self.get_matrix(t)
        cv2.imshow('the environment', self.visualisation)
        cv2.waitKey(1)

    def close(self):
        #opencv on mac hack
        for i in range(5):

            cv2.destroyAllWindows()
            cv2.waitKey(1)


class Waves_np:
    def __init__(self, pos, dims, f, theta, wave_length, direction, thresh):

        self.dims = dims
        self.x = np.linspace(0, self.dims[1], self.dims[1])
        self.y = np.linspace(0, self.dims[0], self.dims[0])

        self.x_grid, self.y_grid = np.meshgrid(self.x, self.y)

        self.visualisation = np.ones((self.dims[0], self.dims[1]), np.float32)
        self.thresh = thresh
        self.f = f
        self.theta = theta
        self.wave_length = wave_length
        self.pos = pos
        self.direction = direction # should be +/- 1
    
    def draw(self):
    	cv2.imshow("decision_making", self.visualisation)
    	cv2.waitKey(1)

    def make_waves(self, t):

        x_part = self.x_grid * np.cos(self.theta)
        y_part = self.y_grid * np.sin(self.theta)
        total_part = x_part + y_part 
        self.visualisation = ((np.sin(np.pi*2 * (total_part / self.wave_length - 
                                                self.direction * self.f*t)) 
                             + 1.0) / 2.0) 
        if self.thresh == True:
            self.visualisation = np.round(self.visualisation)

        return self.visualisation #* 255 #times 255 for opencv uint8 vis

    def run(self):
        self.graphics()

    def close(self):
        #opencv on mac hack
        for i in range(5):

            cv2.destroyAllWindows()
            cv2.waitKey(1)


