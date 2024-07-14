import os
import argparse

def rename_files(directory, recursive, format):
    for root, _, files in os.walk(directory):
        for file in files:
            # 分离文件名和扩展名
            base, ext = os.path.splitext(file)
            if '／' in base or ' - ' in base:
                old_name = os.path.join(root, file)
                new_base = base

                if format == 'a' and '／' in base:
                    parts = base.split('／')
                    new_base = f"{parts[1]} - {parts[0]}"
                elif format == 's' and ' - ' in base:
                    parts = base.split(' - ')
                    new_base = f"{parts[1]}／{parts[0]}"
                elif format == 'o':
                    if '／' in base:
                        parts = base.split('／')
                        new_base = f"{parts[1]} - {parts[0]}"
                    elif ' - ' in base:
                        parts = base.split(' - ')
                        new_base = f"{parts[1]}／{parts[0]}"

                new_name = os.path.join(root, new_base + ext)

                if old_name != new_name:
                    print(f'Renaming "{old_name}" to "{new_name}"')
                    os.rename(old_name, new_name)
        
        if not recursive:
            break

def main():
    parser = argparse.ArgumentParser(description="Rename files in a directory.")
    parser.add_argument("-i", type=str, required=True, help="Directory containing the files to rename.")
    parser.add_argument("-m", type=int, choices=[0, 1], default=0, help="Include subdirectories: 1 for yes, 0 for no (default: 0).")
    parser.add_argument("-f", type=str, choices=['a', 's', 'o'], default='o', help="Format: 'a' for AAA/BBB to BBB - AAA, 's' for BBB - AAA to AAA/BBB, 'o' to swap formats (default: 'o').")

    args = parser.parse_args()

    rename_files(args.i, args.m == 1, args.f)

print("By yzxz&ChatGPT-4o\n\n-i 参数指定要处理的文件夹路径\n-m 参数设置为1表示递归处理子文件夹，设置为0表示不递归\n-f 参数设置为a表示将AAA\BBB格式改为BBB - AAA，设置为s表示将BBB - AAA格式改为AAA\BBB，设置为o表示相反格式转换\n")
if __name__ == "__main__":
    main()
