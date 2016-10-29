import MoLS
import matlab

My_test=MoLS.initialize()
directory = '../daymetData'
files = [f for f in listdir(directory) if isfile(join(directory, f))]
for f in files:
	My_test.MoLS('../daymetData/'+f,'Test_Data',nargout=0)
My_test.terminate()    
