<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Laravel Landing Page</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .navbar {
            background-color: #f8f9fa; /* Light background for navbar */
        }
        .carousel-item img {
            height: 500px; /* Adjust as needed */
            object-fit: cover;
        }
        .burgundy-strip {
            background-color: #800020; /* Burgundy color */
            height: 50px; /* Adjust as needed */
        }
        .parallax {
            background-attachment: fixed;
            background-position: center;
            background-repeat: no-repeat;
            background-size: cover;
            height: 800px; /* Adjust as needed */
            display: flex;
            justify-content: center;
            align-items: center;
            color: white;
            text-align: center;
        }
        .parallax-1 {
            background-image: url('your-parallax-image-1.jpg'); /* Replace with your image */
        }
        .parallax-2 {
            background-image: url('your-parallax-image-2.jpg'); /* Replace with your image */
        }
        .footer {
            background-color: #343a40; /* Dark background for footer */
            color: white;
            padding: 20px 0;
            text-align: center;
        }
    </style>
</head>
<body>

    <nav class="navbar navbar-expand-lg">
        <div class="container">
            <a class="navbar-brand" href="#">Your Logo</a>
            <div class="collapse navbar-collapse">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item"><a class="nav-link" href="#">Home</a></li>
                    <li class="nav-item"><a class="nav-link" href="#">About</a></li>
                    <li class="nav-item"><a class="nav-link" href="#">Contact</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <div id="imageCarousel" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-inner">
            <div class="carousel-item active">
                <img src="your-carousel-image-1.jpg" class="d-block w-100" alt="Carousel Image 1">
            </div>
            <div class="carousel-item">
                <img src="your-carousel-image-2.jpg" class="d-block w-100" alt="Carousel Image 2">
            </div>
            </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#imageCarousel" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#imageCarousel" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
        </button>
    </div>

    <div class="burgundy-strip"></div>

    <div class="parallax parallax-1">
        <h1>Parallax Section 1</h1>
        <p>Your content here...</p>
    </div>

    <div class="parallax parallax-2">
        <h1>Parallax Section 2</h1>
        <p>Your content here...</p>
    </div>

    <footer class="footer">
        <p>&copy; {{ date('Y') }} Your Company. All rights reserved.</p>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>