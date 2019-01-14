This script takes the average pixel color of images in the input and produces the result as a .png output.

To set up, I recommend using a virtual environment:

```bash
git clone https://github.com/ulrikah/image-mani.git && cd image-mani
python -m venv .
source bin/activate
pip install -r requirements.txt
```

When everything is installed, simply run `python pixel.py`. The output image is found in `assets/new_face.png`.


I have been using this dataset [http://people.eecs.berkeley.edu/~shiry/projects/yearbooks/yearbooks.html](http://people.eecs.berkeley.edu/~shiry/projects/yearbooks/yearbooks.html) when developing. Simply place your desired images in `assets/test_data/` if you want to change this.


### Example:
Below are the output images when comparing all women and men, respectively, from years 2000-2013 from the given dataset.

![avg. woman from 2000s](assets/avg_all_women_from_2000s.png)


![avg. man from 2000s](assets/avg_all_men_from_2000s.png)

