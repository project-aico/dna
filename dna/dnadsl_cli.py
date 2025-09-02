#!/usr/bin/env python3
import argparse
import yaml

# -----------------------
# DNA ↔ 二进制映射（每碱基2bit）
# -----------------------
DNA_TO_BIN = {'A':'00','C':'01','G':'10','T':'11'}
BIN_TO_DNA = {v:k for k,v in DNA_TO_BIN.items()}

# -----------------------
# 编码/解码函数
# -----------------------
def utf8_to_dna(text: str) -> str:
    dna_seq = ''
    for byte in text.encode('utf-8'):
        bin_str = f"{byte:08b}"
        # 每2 bit映射成1个碱基，共4碱基 = 1 byte
        for i in range(0,8,2):
            dna_seq += BIN_TO_DNA[bin_str[i:i+2]]
    return dna_seq

def dna_to_utf8(dna_seq: str) -> str:
    bits = ''
    for base in dna_seq:
        bits += DNA_TO_BIN[base]
    # 按8bit拆分成字节
    bytes_list = []
    for i in range(0,len(bits),8):
        byte_bits = bits[i:i+8]
        if len(byte_bits)<8:
            byte_bits = byte_bits.ljust(8,'0')
        bytes_list.append(int(byte_bits,2))
    return bytes(bytes_list).decode('utf-8')

# -----------------------
# DNADSL 文件操作
# -----------------------
def save_dnadsl(filename, dna_seq, metadata):
    data = {
        'dnadsl_version':'1.0',
        'metadata': metadata,
        'sequence': dna_seq
    }
    with open(filename,'w',encoding='utf-8') as f:
        yaml.dump(data,f,allow_unicode=True)

def load_dnadsl(filename):
    with open(filename,'r',encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data.get('metadata',{}), data.get('sequence','')

# -----------------------
# 命令行操作
# -----------------------
def encode_command(args):
    text = ''
    if args.input_file:
        with open(args.input_file,'r',encoding='utf-8') as f:
            text = f.read()
    elif args.text:
        text = args.text
    else:
        print("Error: provide --text or --input_file")
        return

    dna_seq = utf8_to_dna(text)
    metadata = {
        'author': args.author or '',
        'encoding': '4base2byte'
    }
    save_dnadsl(args.output,dna_seq,metadata)
    print(f"DNADSL file saved to {args.output}")

def decode_command(args):
    metadata,dna_seq = load_dnadsl(args.input)
    text = dna_to_utf8(dna_seq)
    print(f"Decoded text:\n{text}")

# -----------------------
# 主程序
# -----------------------
def main():
    parser = argparse.ArgumentParser(description='DNADSL CLI (4-base → 1 byte)')
    subparsers = parser.add_subparsers(dest='command')

    # encode
    encode_parser = subparsers.add_parser('encode',help='Encode text to DNADSL YAML')
    encode_parser.add_argument('--text',type=str,help='Text to encode')
    encode_parser.add_argument('--input_file',type=str,help='Input text file')
    encode_parser.add_argument('--output',type=str,required=True,help='Output YAML file')
    encode_parser.add_argument('--author',type=str,help='Author metadata')
    encode_parser.set_defaults(func=encode_command)

    # decode
    decode_parser = subparsers.add_parser('decode',help='Decode DNADSL YAML to text')
    decode_parser.add_argument('--input',type=str,required=True,help='Input DNADSL YAML file')
    decode_parser.set_defaults(func=decode_command)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return
    args.func(args)

if __name__ == "__main__":
    main()
