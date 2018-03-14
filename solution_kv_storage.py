import json
import argparse
import os
import tempfile

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

parser = argparse.ArgumentParser()
parser.add_argument("--key", "--k", type=str, help="gets key")
parser.add_argument("--value", "--val", "--v", type=str, help="gets value")
args = parser.parse_args()

if args.key and args.value:
	if os.path.isfile(storage_path):
		with open(storage_path, 'r') as f:
			data = f.read()
			loaded = json.loads(data) if data else dict()
	else:
		loaded = dict()
	with open(storage_path, 'w') as f:		
		if args.key in loaded: 
			loaded[args.key].append(args.value)
		else:
			loaded[args.key] = [args.value]
		json.dump(loaded, f)
elif args.key:
	if os.path.isfile(storage_path):
		with open(storage_path, 'r') as f:
			data = f.read()
			loaded = json.loads(data).get(args.key) if data else None
			print(', '.join(map(str, loaded))) if loaded else print(loaded)