
import pytest

from silsilah_organisasi.node import EmployeeNode
from silsilah_organisasi.tree import OrganizationTree
from silsilah_organisasi.sample_data import build_sample_tree


# 1. Pengujian insert_node
def test_insert_node():
    tree = build_sample_tree()

    new_node = tree.insert_node(
        "P006",
        "P019",
        "Dewi",
        "Dosen"
    )

    assert new_node.employee_id == "P019"
    assert new_node.parent.employee_id == "P006"


# 2. Pengujian pencarian berdasarkan nama
def test_search_by_name():
    tree = build_sample_tree()

    results = tree.search_node("Wakil Rektor I")

    assert len(results) == 1
    assert results[0].name == "Wakil Rektor I"


# 3. Pengujian pencarian berdasarkan jabatan
def test_search_by_position():
    tree = build_sample_tree()

    results = tree.search_node("Koordinator Dosen")

    assert len(results) == 1
    assert results[0].position == "Koordinator Dosen"


# 4. Pengujian ID duplikat
def test_duplicate_id():
    tree = build_sample_tree()

    with pytest.raises(ValueError):
        tree.insert_node(
            "P001",
            "P002",
            "Nama Baru",
            "Dosen"
        )


# 5. Pengujian atasan tidak ditemukan
def test_parent_not_found():
    tree = build_sample_tree()

    with pytest.raises(ValueError):
        tree.insert_node(
            "P999",
            "P020",
            "Nama Baru",
            "Dosen"
        )


# 6. Pengujian preorder traversal
def test_preorder():
    tree = build_sample_tree()

    result = [
        node.employee_id
        for node in tree.preorder()
    ]

    assert result == [
        "P001",
        "P002", "P003", "P004", "P005", "P006",
        "P007", "P008", "P009", "P010",
        "P011", "P012", "P014", "P015",
        "P013", "P016", "P017", "P018"
    ]


# 7. Pengujian inorder traversal
def test_inorder():
    tree = build_sample_tree()

    result = [
        node.employee_id
        for node in tree.inorder()
    ]

    assert result == [
        "P002", "P001", "P003", "P004", "P005",
        "P007", "P006", "P008", "P009",
        "P011", "P010",
        "P014", "P012", "P015",
        "P017", "P016", "P013", "P018"
    ]


# 8. Pengujian postorder traversal
def test_postorder():
    tree = build_sample_tree()

    result = [
        node.employee_id
        for node in tree.postorder()
    ]

    assert result == [
        "P002", "P003", "P004", "P005",
        "P007", "P008", "P009",
        "P011", "P014", "P015", "P012",
        "P017", "P016", "P018", "P013",
        "P010", "P006", "P001"
    ]


# 9. Pengujian root
def test_root():
    root = EmployeeNode(
        "P001",
        "Rektor",
        "Rektor"
    )

    tree = OrganizationTree(root)

    assert tree.root == root
    assert tree.root.parent is None
