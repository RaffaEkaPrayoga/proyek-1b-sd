
from .node import EmployeeNode
from .tree import OrganizationTree


def build_sample_tree():
    # ROOT: REKTOR
    root = EmployeeNode(
        "P001",
        "Rektor",
        "Rektor"
    )

    tree = OrganizationTree(root)

    # LEVEL 1: BAWAHAN REKTOR
    tree.insert_node(
        "P001", "P002",
        "Senat Universitas",
        "Senat Universitas"
    )

    tree.insert_node(
        "P001", "P003",
        "Wakil Rektor I",
        "Bidang Akademik"
    )

    tree.insert_node(
        "P001", "P004",
        "Wakil Rektor II",
        "Bidang Administrasi Umum & Keuangan"
    )

    tree.insert_node(
        "P001", "P005",
        "Wakil Rektor III",
        "Bidang Kemahasiswaan & Kerja Sama"
    )

    tree.insert_node(
        "P001", "P006",
        "Dekan Fakultas Sains dan Teknologi",
        "Dekan"
    )

    # LEVEL 2: BAWAHAN DEKAN
    tree.insert_node(
        "P006", "P007",
        "Wakil Dekan I",
        "Bidang Akademik & Kelembagaan"
    )

    tree.insert_node(
        "P006", "P008",
        "Wakil Dekan II",
        "Bidang AUPK"
    )

    tree.insert_node(
        "P006", "P009",
        "Wakil Dekan III",
        "Bidang Kemahasiswaan"
    )

    tree.insert_node(
        "P006", "P010",
        "Ketua Program Studi Teknik Informatika",
        "Ketua Program Studi"
    )

    # LEVEL 3: BAWAHAN KETUA PROGRAM STUDI
    tree.insert_node(
        "P010", "P011",
        "Sekretaris Program Studi",
        "Sekretaris Program Studi"
    )

    tree.insert_node(
        "P010", "P012",
        "Kepala Laboratorium Komputer",
        "Kepala Laboratorium"
    )

    tree.insert_node(
        "P010", "P013",
        "Koordinator Dosen",
        "Koordinator Dosen"
    )

    # LEVEL 4: BAWAHAN KEPALA LABORATORIUM
    tree.insert_node(
        "P012", "P014",
        "Asisten Laboratorium",
        "Asisten Laboratorium"
    )

    tree.insert_node(
        "P012", "P015",
        "Teknisi Laboratorium",
        "Teknisi Laboratorium"
    )

    # LEVEL 4: BAWAHAN KOORDINATOR DOSEN
    tree.insert_node(
        "P013", "P016",
        "Dosen Pembimbing Akademik",
        "Dosen Pembimbing Akademik"
    )

    tree.insert_node(
        "P013", "P018",
        "Dosen Pengampu Mata Kuliah",
        "Dosen Pengampu Mata Kuliah"
    )

    # LEVEL 5: MAHASISWA BIMBINGAN
    tree.insert_node(
        "P016", "P017",
        "Mahasiswa Bimbingan",
        "Mahasiswa Bimbingan"
    )

    return tree
