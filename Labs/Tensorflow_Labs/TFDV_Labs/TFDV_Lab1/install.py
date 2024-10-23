pip3 install --upgrade virtualenv
python3 -m venv my_tfx
source my_tfx/bin/activate
pip install --upgrade pip setuptools wheel
pip install ml-metadata==1.11.0
pip install tfx==1.14.0 --no-dependencies
python -c "import tfx;print(tfx.version)"