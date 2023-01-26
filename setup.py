from pathlib import Path

import setuptools

version_path = Path(__file__, '..', 'VERSION').resolve()
requirements_path = Path(__file__, '../src/cloud_watch_logs', 'requirements.txt').resolve()

with version_path.open('r') as f:
    VERSION = f.read().strip()

with requirements_path.open('r') as f:
    install_requires = [r.strip() for r in f.read().strip().splitlines()]

setuptools.setup(
    name="cloud_watch_logs",  # 배포되는 package 이름
    version=VERSION,
    author="hwangyoungjae",
    author_email="dudwo56@gmail.com",
    # description="description",
    url="https://github.com/hwangyoungjae/cloud_watch_logs",
    project_urls={
        "cloud_watch_logs": "https://github.com/hwangyoungjae/cloud_watch_logs",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=install_requires,
)
