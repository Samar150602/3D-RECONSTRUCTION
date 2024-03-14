import open3d as o3d

# Load point cloud from file
pcd_file_path = "model.pcd"
point_cloud = o3d.io.read_point_cloud(pcd_file_path)

# Visualize the point cloud
o3d.visualization.draw_geometries([point_cloud])
