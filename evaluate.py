import optparse
from ml import RatioEstimator
from ml.utils.loading import Loader

parser = optparse.OptionParser(usage="usage: %prog [opts]", version="%prog 1.0")
parser.add_option('-s', '--samples',  action='store', type=str, dest='samples', default='qsf', help='samples to derive weights for. default QSF down to QSF up')
(opts, args) = parser.parse_args()
do = opts.samples

loading = Loader()
carl = RatioEstimator()
carl.load('models/'+do+'_carl')
evaluate = ['train', 'val']
for i in evaluate:
    r_hat, _ = carl.evaluate(x='data/'+do+'/X0_'+i+'.npy')
    w = 1./r_hat
    loading.load_result(x0='data/'+do+'/X0_'+i+'.npy',     
                        x1='data/'+do+'/X1_'+i+'.npy',
                        weights=w, 
                        label = i,
                        do = do,
                        save = True,
    )
carl.evaluate_performance(x='data/'+do+'/X_val.npy',y='data/'+do+'/y_val.npy')
