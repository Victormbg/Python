if __name__ == '__main__':
    import cpuinfo
    info = cpuinfo.get_cpu_info()
    print(info)


# NOTE: Pyinstaller may spawn infinite processes if __main__ is not used
if __name__ == '__main__':
    import cpuinfo
    from multiprocessing import freeze_support

    # NOTE: Pyinstaller also requires freeze_support
    freeze_support()
    info = cpuinfo.get_cpu_info()
    print(info)