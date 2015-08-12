package com.born2code.spring.aop;

import org.springframework.stereotype.Component;

@Component("camera")
public class Camera implements PhotoSnapper, ICamera {
    @Override
    public void snap() {
        System.out.println("SNAP");
    }

    @Override
    public void snap(int i) {
        System.out.println("Snap Exposure is: " + i);
    }

    @Override
    public void snap(String s) {
        System.out.println("Snap name is: " + s);
    }

    @Override
    @Deprecated
    public void snapNightTime() {
        System.out.println("SNAP! Night mode.");
    }

    public void snapCar(Car car) {
        System.out.println("Snapping car");
    }
}
