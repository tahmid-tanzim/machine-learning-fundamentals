package com.born2code.spring.aop;

import org.springframework.stereotype.Component;

@Component
public class Camera implements PhotoSnapper, ICamera {
    public void snap() {
        System.out.println("SNAP");
    }
}
