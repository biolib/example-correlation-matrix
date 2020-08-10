import matplotlib.pyplot as plt
import pandas as pd 
import argparse
import base64

def corr_mat(df, corm, color, r=150, show=True, dim=(5, 4), axtickfontsize=9, ar=90, figtype='png'):
    d_corr = df.corr(method=corm)
    # Save
    output = open('output_mat.csv', 'w')
    output.write(str(d_corr))
    output.close()

    plt.subplots(figsize=dim)
    plt.matshow(d_corr, vmin=-1, vmax=1, cmap=color)
    plt.colorbar(shrink=0.75)
    cols = list(df)
    ticks = list(range(0, len(list(df))))
    plt.title('Correlation matrix')
    plt.xticks(ticks, cols, fontsize=axtickfontsize, rotation=ar)
    plt.yticks(ticks, cols, fontsize=axtickfontsize, )
    # Save
    plt.savefig('corr_mat.png', format='png', bbox_inches='tight', dpi=r)

    # Generate the Markdown preview
    file_data = open("corr_mat.png", "rb").read()
    data = base64.b64encode(file_data).decode('ascii')
    print('![picture](data:{};base64,{})'.format('image/png', data))
    # Print to screen
    print('\nCorrelation matrix: \n\n ```', d_corr)

# Load input data
parser = argparse.ArgumentParser()
parser.add_argument('--infile', help = 'dataframe', dest = 'infile')
parser.add_argument('--method', help = 'Correlation method', dest = 'method', default="pearson")
parser.add_argument('--color', help = 'Color scale', dest = 'color_scale', default="seismic")
args = parser.parse_args()

df = pd.read_csv(args.infile)
corm = args.method
color = args.color_scale

corr_mat(df, corm, color)
