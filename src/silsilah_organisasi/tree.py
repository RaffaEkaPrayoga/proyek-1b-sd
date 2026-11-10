
from .node import EmployeeNode


class OrganizationTree:
    def __init__(self, root):
        self.root = root

    # Mencari node berdasarkan ID
    def _find_by_id(self, employee_id):
        for node in self.preorder():
            if node.employee_id.lower() == employee_id.lower():
                return node
        return None

    # 1. INSERT NODE
    def insert_node(self, parent_id, employee_id, name, position):
        # Validasi data
        if not all(value.strip() for value in
                   [parent_id, employee_id, name, position]):
            raise ValueError("Semua data wajib diisi.")

        # Memeriksa ID duplikat
        if self._find_by_id(employee_id):
            raise ValueError("ID pegawai sudah digunakan.")

        # Mencari atasan
        parent = self._find_by_id(parent_id)

        if parent is None:
            raise ValueError("Atasan tidak ditemukan.")

        # Membuat node baru
        new_node = EmployeeNode(
            employee_id,
            name,
            position
        )

        # Menghubungkan node dengan atasan
        parent.add_child(new_node)

        return new_node

    
    # 2. SEARCH NODE
    def search_node(self, keyword):
        results = []

        def traverse(node):
            if node is None:
                return

            if (keyword.lower() == str(node.employee_id).lower() or
                keyword.lower() == node.name.lower()):
                results.append(node)

            for child in node.children:
                traverse(child)

        traverse(self.root)

        return results

    # 3. PREORDER TRAVERSAL
    # Root -> Children
    def preorder(self):
        result = []

        def traverse(node):
            result.append(node)

            for child in node.children:
                traverse(child)

        traverse(self.root)

        return result

    # 4. INORDER TRAVERSAL
    # First Child -> Root -> Remaining Children
    def inorder(self):
        result = []

        def traverse(node):
            if node.children:
                traverse(node.children[0])

            result.append(node)

            for child in node.children[1:]:
                traverse(child)

        traverse(self.root)

        return result

    # 5. POSTORDER TRAVERSAL
    # Children -> Root
    def postorder(self):
        result = []

        def traverse(node):
            for child in node.children:
                traverse(child)

            result.append(node)

        traverse(self.root)

        return result

    # 6. DISPLAY STRUCTURE
    def display_structure(self):
        lines = []

        def traverse(node, level):
            indent = "    " * level

            lines.append(f"{indent}- {node}")

            for child in node.children:
                traverse(child, level + 1)

        traverse(self.root, 0)

        return "\n".join(lines)
