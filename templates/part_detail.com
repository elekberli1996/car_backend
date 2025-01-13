{% extends "base.html" %}
{% load static %}
{% block page_title %}Detay{% endblock page_title %}


{% block custom_css %}
<link rel="stylesheet" href="{% static 'css/car_detail/style.css' %}">
<link rel="stylesheet" href="{% static 'css/car_detail/responsive.css'%}">

{% endblock custom_css %}

{% block page_content %}

<div class="container">

    <div class="car_detail">

        <div class="left">
            <div class="slider_wrapper">
                <div class="slider-container">
                    <!-- her sekil bir bura bir de kicik sekiller hissesine gelmelidi -->
                    <div class="slider">
                        <div class="slide active"><img src="{{ part.main_img.url}}" alt="Image 1"></div>

                         {% for image in images  %}
                            <div class="slide"><img src="{{ image.image.url }}" alt="Image 4"></div>
                        {% endfor %} 
                        
                    </div>

                    <button class="arrow leftSlider">&#10094;</button>
                    <button class="arrow rightSlider">&#10095;</button>

                    <!-- Kiçik şəkillər -->
                    <div class="thumbnails">
                        <div class="tubnail1">
                                    <img class="thumbnail" src="{{ part.main_img.url}}" alt="Image 1">
                                    {% for image in images  %}<img class="thumbnail" src="{{ image.image.url }}" alt="Image 4">
                                    {% endfor %}
                                                           
                        </div>
                       

                    </div>
                </div>
            </div>



            <div class="main_data">
                
                
                
                <div class="lokasiya">
                    <i class="fa-solid fa-location-dot"></i>
                    <span>{{ part.part_name }} </span>
                </div>
            </div>
            <p id="baxis">Elana Baxış sayı: <span id="baxis_value">5432</span></p>
            <hr>
            <div class="additional-data">
                <div class="top">
                    <div class="col">

                        <div class="box">
                            <ul>
                                <li><span id="marka">Marka:</span></li>
                                <li><span id="model">Model:</span></li>
                                <li><span id="location">Yer:</span></li>
                                <li><span id="cond">Vəziyyəti:</span></li>
                                <li><span id="price">Qiymət:</span></li>
                                <li><span id="tel">Tel:</span></li>
                                <li><span id="created">Yükləndi:</span></li>
                               
                            </ul>
                            <ul>
                                <li>
                                    <p id="marka-value">{{ part.brand }}</p>
                                </li>
                                <li>
                                    <p id="model-value">{{ part.model }}</p>
                                </li>
                                <li>
                                    <p id="location-value">{{ part.city }}</p>
                                </li>
                                <li>
                                    <p id="cond-value">{{ part.cond }}</p>
                                </li>
                                <li>
                                    <p id="price-value">{{ part.price}} &nbsp;  {{ part.currency}}</p>
                                </li>
                                <li>
                                    <p id="tel-value">{{ part.tel }}</p>
                                </li>
                                <li>
                                    <p id="created-value">{{ part.created_at }}</p>
                                </li>
                               
                                
                        
                            </ul>
                        </div>
                    </div>
                    
                </div>
                <hr>
                <div class="bottom">
                    <div class="elave_melumat">
                        <span id="melumat">Əlavə məlumat</span>
                        <hr>
                        <p id="melumat_value">{{ part.information }}</p>
                    </div>
                </div>
            </div>

        </div>
        <div class="right">
            <div class="box">
                <p id="qiymet">25 555 AZN</p>
                <hr>




                <div class="ownerinfo">
                    <div class="owner-left">
                        <h1 id="owner"> Random</h1>
                        <p id="city">Naxçıvan</p>
                    </div>

                    <div class="owner-right">
                        <img src="img/pp.jpg" alt="">
                    </div>
                </div>
                <hr>
                <div class="cntctbtn">
                    <button> Əlaqə nömrəsi: <br> 050-505-05-05 </button>
                </div>


            </div>
            <div class="forAdvertising">
                <p>Burada reklamınız ola bilər</p>
            </div>
        </div>


    </div>

</div>
   
{% endblock page_content %}


{% block custom_js %}
<script src="{% static "js/part_detail/app.js" %}"></script>
{% endblock custom_js %}