
import pytest

from silsilah_organisasi.node import EmployeeNode
from silsilah_organisasi.tree import OrganizationTree
from silsilah_organisasi.main import build_sample_tree


# 1. Pengujian insert_node
def test_insert_node():
    tree = build_sample_tree()

    new_node = tree.insert_node(
        "P006",
        "P009",
        "Dewi",
        "Dosen"
    )

    assert new_node.employee_id == "P009"
    assert new_node.parent.employee_id == "P006"


# 2. Pengujian pencarian berdasarkan nama
def test_search_by_name():
    tree = build_sample_tree()

    results = tree.search_node("Rina")

    assert len(results) == 1
    assert results[0].name == "Rina"


# 3. Pengujian pencarian berdasarkan jabatan
def test_search_by_position():
    tree = build_sample_tree()

    results = tree.search_node("Dosen")

    assert len(results) == 1
    assert results[0].position == "Dosen"


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
            "P010",
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
        "P001", "P002", "P003", "P004",
        "P005", "P007", "P008", "P006"
    ]


# 7. Pengujian inorder traversal
def test_inorder():
    tree = build_sample_tree()

    result = [
        node.employee_id
        for node in tree.inorder()
    ]

    assert result == [
        "P002", "P001", "P003", "P007",
        "P005", "P008", "P004", "P006"
    ]


# 8. Pengujian postorder traversal
def test_postorder():
    tree = build_sample_tree()

    result = [
        node.employee_id
        for node in tree.postorder()
    ]

    assert result == [
        "P002", "P003", "P007", "P008",
        "P005", "P006", "P004", "P001"
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
