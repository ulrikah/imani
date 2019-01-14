This script takes the average pixel color of images in the input and produces the result as a .png output.

To set up, I recommend using a virtual environment:

```bash
git clone https://github.com/ulrikah/image-mani.git && cd image-mani
python -m venv .
source bin/activate
pip install -r requirements.txt
```

When everything is installed, simply run `python pixel.py`. The output image is found in `assets/new_face.png`.


I have been using [this dataset](http://people.eecs.berkeley.edu/~shiry/projects/yearbooks/yearbooks.html) when developing. Simply place your desired images in `assets/test_data/` if you want to change this.
