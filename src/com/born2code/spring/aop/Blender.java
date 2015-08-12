package com.born2code.spring.aop;

import org.springframework.stereotype.Component;

@Component
public class Blender implements IBlender {
    @Override
    public void blend() {
        System.out.println("Blending ...");
    }
}
