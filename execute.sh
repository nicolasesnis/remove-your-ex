cd lama
export TORCH_HOME=$(pwd) && export PYTHONPATH=$(pwd)
python3 bin/predict.py refine=True model.path=$(pwd)/big-lama indir=$(pwd)/input outdir=$(pwd)/output
