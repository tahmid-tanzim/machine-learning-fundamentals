package com.born2code.spring.aop;

import org.springframework.stereotype.Component;

@Component
public class Camera {
    public void snap() throws Exception {
        System.out.println("SNAP");
        throw new Exception("Bye Bye Ta ta ...");
    }
}
