import json
import subprocess
import sys
import platform
import urllib.request
import os


def help():
    print("BAAH env checker")
    print("BAAH环境检查器")
    print("")
    print("用法: python3 checker.py <功能> <选项>")
    print("功能:")
    print("  fix - 尝试修复环境")
    print("  check - 检查环境并生成报告")
    print("  help - 显示帮助信息")
    print("  version - 显示版本信息")
    print("选项:")
    print("  当使用 check 功能时:")
    print("    system - 检查系统环境")
    print("    python - 检查Python环境")
    print("  当使用 fix 功能时:")
    print("    all - 修复所有")
    print("    requirements - 修复requirements.txt")


# 定义一个名为version的函数
def version():
    print("BAAH env checker 1.0.0")
    print("BAAH环境检查器 1.0.0")


if __name__ == "__main__":
    # 检查命令行参数长度
    if len(sys.argv) >= 2:
        # 如果命令行参数为version，则调用version()函数
        if sys.argv[1] == "version":
            version()
        # 如果命令行参数为help，则调用help()函数
        elif sys.argv[1] == "help":
            help()
        # 如果命令行参数为check，则检查系统环境
        elif sys.argv[1] == "check":
            # 检查命令行参数长度
            if len(sys.argv) >= 3:
                # 如果命令行参数为system，则调用version()函数
                if sys.argv[2] == "system":
                    version()
                    report = {}
                    report["error"] = []
                    # 检查架构
                    arch_data = json.loads(urllib.request.urlopen(f"https://github.com/BlockHaity/BAAH-env-checker/raw/refs/heads/main/data/arch.json").read().decode("utf-8"))
                    if arch_data.get(platform.machine()) == "support":
                        print(f"架构: {platform.machine()}")
                        report["arch"] = platform.machine()
                    elif arch_data.get(platform.machine()) == "experimental-support":
                        print(f"架构: {platform.machine()} (实验性支持)")
                        report["arch"] = platform.machine()
                        report["error"].append("arch-experimental-support")
                    else:
                        print(f"架构: {platform.machine()} (不支持)")
                        report["arch"] = platform.machine()
                        report["error"].append("arch-not-support")
                    # 检查系统环境
                    if sys.platform == "win32":
                        report["system"] = "Windows"
                        print("系统: Windows")
                        # 检查Windows版本
                        if sys.getwindowsversion().major < 10:
                            print(f"Windows版本: {sys.getwindowsversion().major}")
                            report["version"] = sys.getwindowsversion().major
                            report["error"].append("system-not-support")
                            # 生成报告
                            with open("report-system.json", "w", encoding="utf-8") as f:
                                json.dump(report, f)
                            print("报告已生成: report-system.json")
                            print("请升级您的Windows版本到10或更高版本。")
                        elif sys.getwindowsversion().major == 10:
                            print(f"Windows版本: {sys.getwindowsversion().major}")
                            report["version"] = sys.getwindowsversion().major
                            print("您的Windows版本为10，可以继续使用。")
                            # 生成报告
                            with open("report-system.json", "w", encoding="utf-8") as f:
                                json.dump(report, f)
                            print("报告已生成: report-system.json")
                        if sys.getwindowsversion().major == 11:
                            print(f"Windows版本: {sys.getwindowsversion().major}")
                            report["version"] = sys.getwindowsversion().major
                            print("您的Windows版本为11，可以继续使用。")
                            # 生成报告
                            with open("report-system.json", "w", encoding="utf-8") as f:
                                json.dump(report, f)
                            print("报告已生成: report-system.json")
                    elif sys.platform == "linux":
                        print("系统: Linux")
                        report["platform"] = "Linux"
                        # 检查Linux发行版
                        if (
                            subprocess.run(
                                ["uname", "-o"], capture_output=True, text=True
                            ).stdout.strip()
                            == "Android"
                        ):
                            print("你的环境为Termux，请参考文档中的博客链接部署。")
                            report["linux_id"] = "Termux"
                            report["error"].append("experimental-support")
                        else:
                            linux_id = subprocess.run(
                                ["lsb_release", "-is"], capture_output=True, text=True
                            ).stdout.strip()
                            linux_id_data = json.loads(
                                urllib.request.urlopen(
                                    f"https://github.com/BlockHaity/BAAH-env-checker/raw/refs/heads/main/data/linux/linux_id_data.json"
                                )
                                .read()
                                .decode("utf-8")
                            )
                            print(f"Linux发行版: {linux_id}")
                            # 检查Linux发行版支持情况
                            if linux_id in linux_id_data:
                                if linux_id_data[linux_id] == "support":
                                    print("您的Linux发行版为支持版本，可以继续使用。")
                                    report["linux_id"] = linux_id
                                    report["error"] = "none"
                                elif linux_id_data[linux_id] == "not-support":
                                    print(
                                        "您的Linux发行版为不支持版本，请更换为支持版本。"
                                    )
                                    report["linux_id"] = linux_id
                                    report["error"].append("system-not-support")
                                elif linux_id_data[linux_id] == "experimental-support":
                                    print(
                                        "您的Linux发行版为实验性支持版本，可以继续使用。"
                                    )
                                    report["linux_id"] = linux_id
                                    report["error"].append("experimental-support")
                            else:
                                print("您的Linux发行版支持情况未知。")
                                report["linux_id"] = linux_id
                                report["error"].append("system-unknown")
                            # 生成报告
                    with open("report-system.json", "w", encoding="utf-8") as f:
                        json.dump(report, f)
                    print("报告已生成: report-system.json")
                elif sys.argv[2] == "python":
                    report = {}
                    report["error"] = []
                    # 检查Python版本
                    if sys.version_info == (3, 10):
                        print("Python版本: 完全支持")
                        report["python"] = sys.version
                        report["error"] = "none"
                    elif sys.version_info > (3, 10):
                        print("Python版本: 部分支持，需要修复requeirements")
                        report["python"] = sys.version
                        report["error"].append("python-need-fix")
                    else:
                        print("Python版本: 不支持")
                        report["python"] = sys.version
                        report["error"].append("python-not-support")
                    # 检查venv模块
                    try:
                        import venv
                        print("venv模块: 支持")
                        report["venv"] = "have"
                    except ImportError:
                        print("venv模块: 不支持")
                        report["venv"] = "not-have"
                        report["error"].append("venv-not-have")
                    report["package"] = []
                    for package in subprocess.run(['pip', 'freeze'], capture_output=True, text=True).stdout.split('\n'):
                        report["package"].append(package)
                    with open("report-python.json", "w", encoding="utf-8") as f:
                        json.dump(report, f)
                    print("报告已生成: report-python.json")
            else:
                help()
            exit(0)
        elif sys.argv[1] == 'fix':
            if len(sys.argv) == 3:
                if sys.argv[2] == 'requeirements':
                    if '--force' in sys.argv:
                        print("正在修复requirements...")
                        os.rename("requirements.txt", "requirements.txt.backup")
                        print("指定--force，强制使用最新版本")
                        urllib.request.urlretrieve("https://github.com/BlockHaity/BAAH-env-checker/raw/refs/heads/main/requirements/force.txt", "requirements.txt")
                        print("修复完成！")
                    elif sys.version_info >= (3, 12, 0) and sys.version_info < (3, 13, 0):
                        print("正在修复requirements...")
                        os.rename("requirements.txt", "requirements.txt.backup")
                        urllib.request.urlretrieve("https://github.com/BlockHaity/BAAH-env-checker/raw/refs/heads/main/requirements/python312.txt", "requirements.txt")
                        print("修复完成！")
                        print("文件变动：requirements.txt  onnxruntime==1.16.9 --> onnxruntime==1.17.0")
                    elif sys.version_info >= (3, 10, 0) and sys.version_info < (3, 11, 0):
                        print("python版本支持完美，无需修复。")
                    elif sys.version_info <= (3, 10, 0):
                        print("python版本过低，无法修复。")
                                        
    else:
        # 如果命令行参数为空，则调用help()函数
        help()
        exit(1)
