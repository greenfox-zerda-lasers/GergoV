var imageCache = [
  {
    url: 'joshua-tree-national-park-74399_1280.jpg',
    title: 'Joshua Tree',
    description: 'Deseret, consectetur adipiscing elit. Maecenas nulla velit, epice sed fringilla eget, faucibus at magna. Etiam eu.'
  },
  {
    url: 'beach-84631_1280.jpg',
    title: 'Sandy beach',
    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas nulla velit, elementum sed fringilla eget, faucibus at magna. Etiam eu.'
  },
  {
    url: 'iceberg-404966_1280.jpg',
    title: 'Iceberg',
    description: 'Lorem ipsum dolor sit amet, Rosenberg adipiscing elit. Maecenas nulla velit, elementum sed fringilla eget, faucibus at magna. Etiam eu.'
  },
  {
    url: 'lake-65443_1280.jpg',
    title: 'Lake',
    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas nulla velit, elementum sed fringilla eget, faucibus at magna. Etiam eu.'
  },
  {
    url: 'prairie-679016_1920.jpg',
    title: 'Prairie',
    description: 'Lorem ipsum dolor sit amet, Texas adipiscing elit. Maecenas nulla velit, elementum sed fringilla eget, armadillo at magna. Etiam eu.'
  },
  {
    url: 'sunset-1700877_1280.jpg',
    title: 'Sunset',
    description: 'Lorem ipsum dolor sit Aztec, consectetur adipiscing elit. Maecenas nulla velit, elementum sed fringilla eget, faucibus at magna. Etiam eu.'
  },
  {
    url: 'the-scenery-679011_1280.jpg',
    title: 'Scenery',
    description: 'Lorem ipsum forest sit amet, consectetur adipiscing elit. Maecenas erosio velit, elementum sed fringilla eget, faucibus at magna. Etiam eu.'
  },
];

function getImageCount () { return imageCache.length; };

var mainImage = document.querySelector('.image-shown');
var mainImageUrl = mainImage.style.backgroundImage;

var button = document.querySelectorAll('.side-nav-button');

var thumbsBar = document.querySelector('.image-thumbnail-bar');

function generateThumbs() {
  imageCache.forEach(function(e) {
    var newThumb = document.createElement('div')
    newThumb.setAttribute('class', 'thumbnail');
    newThumb.style.backgroundImage = "url('./images/" + e.url + "');";
    // insert img
    thumbsBar.appendChild(newThumb);
  });
};

generateThumbs();
