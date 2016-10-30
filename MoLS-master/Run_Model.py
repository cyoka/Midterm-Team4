import MoLS
import matlab


My_test=MoLS.initialize()
My_test.MoLS('./test_data','32.2284_-110.1085.csv',nargout=0)
My_test.terminate()    
