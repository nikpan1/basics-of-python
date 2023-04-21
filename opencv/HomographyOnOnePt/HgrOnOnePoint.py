        # https://stackoverflow.com/questions/52653346/how-to-find-a-point-after-wraptransform
        before_transformation = np.float32([[[pt[0], pt[1]]]])
        after_tranformation = np.squeeze(cv.perspectiveTransform(before_transformation, M))
