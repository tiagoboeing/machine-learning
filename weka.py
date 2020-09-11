from os import listdir
from os.path import isfile, join

class Weka():
  def __init__(self, images_directory):
    self.images_directory = images_directory
    self.header = '''
    @relation caracteristicas\n\n
    @attribute laranja_camisa_bart real\n
    @attribute azul_calcao_bart real\n
    @attribute azul_sapato_bart real\n
    @attribute marrom_boca_homer real\n
    @attribute azul_calca_homer real\n
    @attribute cinza_sapato_homer real\n
    @attribute classe {Bart, Homer}\n\n
    @data\n'''

  def list_directory_files(self):
    onlyfiles = [f for f in listdir(self.images_directory) if isfile(join(self.images_directory, f))]
    return onlyfiles


  def extract(self):
    self.list_directory_files()
