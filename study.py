
from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D



corners=np.array([])
fig = plt.figure()
ax = Axes3D(fig)

obj = np.array(  [[[ 0,1,0],[1,1,0],[1,1,1],[0,1,1],[ 0,0,0],[1,0,0],[1,0,1],[0,0,1] ]]
                )

# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)

Z =obj[:,:,2]
print(Z)
X, Y=obj[:,:,0],obj[:,:,1]
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')

plt.show()



def get_bdb_form_from_corners(corners):
    vec_0 = (corners[:, 2, :] - corners[:, 1, :]) / 2.
    vec_1 = (corners[:, 0, :] - corners[:, 4, :]) / 2.
    vec_2 = (corners[:, 1, :] - corners[:, 0, :]) / 2.

    coeffs_0 = np.linalg.norm(vec_0, axis=1)
    coeffs_1 = np.linalg.norm(vec_1, axis=1)
    coeffs_2 = np.linalg.norm(vec_2, axis=1)
    coeffs = np.stack([coeffs_0, coeffs_1, coeffs_2], axis=1)

    centroid = (corners[:, 0, :] + corners[:, 6, :]) / 2.

    basis_0 = np.dot(np.diag(1 / coeffs_0), vec_0)
    basis_1 = np.dot(np.diag(1 / coeffs_1), vec_1)
    basis_2 = np.dot(np.diag(1 / coeffs_2), vec_2)

    basis = np.stack([basis_0, basis_1, basis_2], axis=1)

    return {'basis': basis, 'coeffs': coeffs, 'centroid': centroid}

# {'basis': array([[[-0.78861266, 0., 0.61489034],
#                   [0., 1., 0.],
#                   [-0.61489034, 0., -0.78861266]],
#
#                  [[0.23315538, 0., -0.97243947],
#                   [0., 1., 0.],
#                   [0.97243947, 0., 0.23315538]],
#
#                  [[-0.04544187, 0., 0.998967],
#                   [0., 1., 0.],
#                   [-0.998967, 0., -0.04544187]],
#
#                  [[0.75614476, 0., 0.6544044],
#                   [0., 1., 0.],
#                   [-0.6544044, 0., 0.75614476]],
#
#                  [[0.8171477, 0., 0.5764284],
#                   [0., 1., 0.],
#                   [-0.5764284, 0., 0.8171477]]], dtype=float32),
#  'centroid': array([[2.093301, -0.88592076, -0.02014118],
#                     [1.2353034, -0.7412901, 0.32869214],
#                     [3.2719235, -0.2072553, -1.1957575],
#                     [3.875805, -0.29349667, -2.0382893],
#                     [2.0365374, -0.80655986, -0.9518025]], dtype=float32),
#  'coeffs': array([[0.31068414, 0.43854204, 0.3469375],
#                   [0.29948983, 0.4299795, 0.36500514],
#                   [0.18744104, 0.35624564, 0.207048],
#                   [0.5196335, 0.6610563, 0.14500004],
#                   [0.61365616, 0.40629333, 0.49402416]], dtype=float32),
#  'class_id': array([5, 5, 35, 16, 7])}
