def pdbFasta(fileName):        
    input_file = open(fileName)
    
    letters = {'ALA':'A','ARG':'R','ASN':'N','ASP':'D','CYS':'C','GLU':'E','GLN':'Q','GLY':'G','HIS':'H',
               'ILE':'I','LEU':'L','LYS':'K','MET':'M','PHE':'F','PRO':'P','SER':'S','THR':'T','TRP':'W',
               'TYR':'Y','VAL':'V'}
    name=(fileName.split('.',1)[0])
    filename=name+'.fasta'
    name='>'+name+'\n';
    f=open(filename,"w+")
    
    f.writelines(name)

    prev = '-1'
    for line in input_file:
        toks = line.split()
        if len(toks)<1: continue
        if toks[0] != 'ATOM': continue
        if toks[3] == 'HOH': continue
        if toks[5] != prev:
            f.write('%c' % letters[toks[3]])
        prev = toks[5]
    
    f.close()
    input_file.close()
