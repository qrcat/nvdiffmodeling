import os
import trimesh

def write_ply_with_vert_color(folder, mesh):
    ply_file = os.path.join(folder, 'mesh.ply')

    v_pos = mesh.v_pos.detach().cpu().numpy() if mesh.v_pos is not None else None
    v_nrm = mesh.v_nrm.detach().cpu().numpy() if mesh.v_nrm is not None else None
    v_tex = mesh.v_tex.detach().cpu().numpy() if mesh.v_tex is not None else None

    v_kd = mesh.v_kd.detach().cpu().numpy() if mesh.v_kd is not None else None

    t_pos_idx = mesh.t_pos_idx.detach().cpu().numpy() if mesh.t_pos_idx is not None else None
    t_nrm_idx = mesh.t_nrm_idx.detach().cpu().numpy() if mesh.t_nrm_idx is not None else None
    t_tex_idx = mesh.t_tex_idx.detach().cpu().numpy() if mesh.t_tex_idx is not None else None

    mesh_trimesh = trimesh.Trimesh(vertices=v_pos, faces=t_pos_idx, vertex_normals=v_nrm, vertex_colors=v_kd)
    _ = mesh_trimesh.export(ply_file)
    print("Done exporting mesh")

def write_ply_with_face_color(folder, mesh):
    ply_file = os.path.join(folder, 'mesh.ply')

    v_pos = mesh.v_pos.detach().cpu().numpy() if mesh.v_pos is not None else None
    v_nrm = mesh.v_nrm.detach().cpu().numpy() if mesh.v_nrm is not None else None
    v_tex = mesh.v_tex.detach().cpu().numpy() if mesh.v_tex is not None else None

    f_kd = mesh.f_kd.detach().cpu().numpy() if mesh.f_kd is not None else None

    t_pos_idx = mesh.t_pos_idx.detach().cpu().numpy() if mesh.t_pos_idx is not None else None
    t_nrm_idx = mesh.t_nrm_idx.detach().cpu().numpy() if mesh.t_nrm_idx is not None else None
    t_tex_idx = mesh.t_tex_idx.detach().cpu().numpy() if mesh.t_tex_idx is not None else None

    mesh_trimesh = trimesh.Trimesh(vertices=v_pos, faces=t_pos_idx, vertex_normals=v_nrm, face_colors=f_kd)
    _ = mesh_trimesh.export(ply_file)
    print("Done exporting mesh")

