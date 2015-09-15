from django.shortcuts import render
import os
# Create your views here.
from main.models import *


# def dicomparser(request):
#
#
#     if os.system("find " + camino + " -maxdepth 6 -name '*.DCM' > /" + camino + "/dclist.txt "):
#         print "Es un dicom"
#     else:
#         print "No es un dicom"
#
#     return



    # lista = ImgContainer.objects.filter(user_id=user.pk).filter(active=True).order_by('id')
    #
    # lista2 = Model.objects.filter(user_id=user.pk).filter(active=True).order_by('id')
    # c1 = {'lista' : lista}
    # c2 = {'lista2' : lista2}
    #
    # context = {}
    # context.update(c1)
    # context.update(c2)

def nhdr2nrrd(id):
    file = ImgContainer.objects.get(pk=id)

    file1 = file.file
    print file1.read()
    file2 = str(file.file) + ".raw.gz"
    output = str(file.file) + ".nrrd"
    with open('retorno','w') as r:
        r.write('\n')
    # files = [file1, 'retorno', file2]
    # with open ('output','w') as outfile:
    #     for fname in files:
    #         with open(fname) as infile:
    #             for line in infile:
    #                 outfile.write(line)

    # return output
    #
    # with open (output, 'w') as outfile