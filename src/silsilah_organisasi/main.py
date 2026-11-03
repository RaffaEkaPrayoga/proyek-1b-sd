
from .sample_data import build_sample_tree

def print_traversal(title, nodes):
    print(f"\n{title}")
    print("-" * 50)

    for index, node in enumerate(nodes, start=1):
        print(f"{index}. {node}")


def main():
    tree = build_sample_tree()

    while True:
        print("\n" + "=" * 55)
        print(" SISTEM MANAJEMEN SILSILAH ORGANISASI")
        print(" UIN SULTAN SYARIF KASIM RIAU")
        print("=" * 55)

        print("1. Tampilkan Struktur Organisasi")
        print("2. Tambahkan Pegawai")
        print("3. Cari Pegawai")
        print("4. Preorder Traversal")
        print("5. Inorder Traversal")
        print("6. Postorder Traversal")
        print("0. Keluar")

        choice = input("\nPilih menu: ").strip()

        # Menu 1: Struktur organisasi
        if choice == "1":
            print("\nSTRUKTUR ORGANISASI")
            print(tree.display_structure())

        # Menu 2: Tambah pegawai
        elif choice == "2":
            print("\nTAMBAH PEGAWAI")

            parent_id = input("ID Atasan: ")
            employee_id = input("ID Pegawai: ")
            name = input("Nama Pegawai: ")
            position = input("Jabatan: ")

            try:
                node = tree.insert_node(
                    parent_id,
                    employee_id,
                    name,
                    position
                )

                print(f"\nBerhasil menambahkan: {node}")

            except ValueError as error:
                print(f"\nGagal: {error}")

        # Menu 3: Pencarian pegawai
        elif choice == "3":
            keyword = input(
                "\nMasukkan nama atau jabatan: "
            )

            results = tree.search_node(keyword)

            if results:
                print(f"\nDitemukan {len(results)} data:")

                for node in results:
                    print(f"- {node}")
            else:
                print("\nData tidak ditemukan.")

        # Menu 4: Preorder
        elif choice == "4":
            print_traversal(
                "PREORDER TRAVERSAL",
                tree.preorder()
            )

        # Menu 5: Inorder
        elif choice == "5":
            print_traversal(
                "INORDER TRAVERSAL",
                tree.inorder()
            )

        # Menu 6: Postorder
        elif choice == "6":
            print_traversal(
                "POSTORDER TRAVERSAL",
                tree.postorder()
            )

        # Menu 0: Keluar
        elif choice == "0":
            print("\nProgram selesai. Terima kasih!")
            break

        else:
            print("\nPilihan tidak valid!")


if __name__ == "__main__":
    main()
