package com.born2code.spring.camera.accessories;

import org.springframework.stereotype.Component;

@Component
public class Lens {
    public void zoom(int factor) {
        System.out.println("Zooming Lens: " + factor);
    }
}
