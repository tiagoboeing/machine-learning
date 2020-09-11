from os import listdir
from os.path import isfile, join
from read_image import ReadImage
from logger import Logger

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
    Logger.log('Reading all folder files')
    onlyfiles = [f for f in listdir(self.images_directory) if isfile(join(self.images_directory, f))]
    Logger.log(f'\n{len(onlyfiles)} images found in {self.images_directory} directory!', True)
    return onlyfiles

  def extract(self):
    imagesData = []
    for index, image in enumerate(list(self.list_directory_files())):
      Logger.log(f'Extracting characteristics from {image}')
      imagesData.append(ReadImage().read(f'{self.images_directory}/{image}'))
      Logger.log(f'Data added to index {index}', True)

    print(imagesData)
