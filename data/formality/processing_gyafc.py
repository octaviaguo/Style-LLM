import os
import glob

gyafc_filenames = ['train', 'tune', 'test']
out_filenames = ['train', 'dev', 'test']
domains = ['Family_Relationships', 'Entertainment_Music']

for infile, outfile in zip(gyafc_filenames, out_filenames):
    fout = open('{}.tsv'.format(outfile), 'w')

    for domain in domains:
        for label in ['formal','informal']:
            with open(os.path.join('./GYAFC_Corpus', domain, infile, label)) as f:
                for line in f:
                    line = line.strip()
                    fout.write('{}\t{}\n'.format(line, label))
    fout.close()
