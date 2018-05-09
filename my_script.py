from pystrich.datamatrix import DataMatrixEncoder

encoder = DataMatrixEncoder('This is a Data Matrix.')

encoder.save('./datamatrix_test.png')

print(encoder.get_ascii())