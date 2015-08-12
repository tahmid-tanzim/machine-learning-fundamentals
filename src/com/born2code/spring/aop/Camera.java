package com.born2code.spring.aop;

import org.springframework.stereotype.Component;

@Component("camera")
public class Camera implements PhotoSnapper, ICamera {
    @Override
    @Deprecated
    public void snap() {
        System.out.println("SNAP");
    }

    @Override
    public void snap(int i) {
        System.out.println("Snap Exposure is: " + i);
    }

    @Override
    public void snap(double exposure) {
        System.out.println("SNAP! Exposure:" + exposure);
    }

    @Override
    public void snap(String s) {
        System.out.println("Snap name is: " + s);
    }

    @Override
    public void snapNightTime() {
        System.out.println("SNAP! Night mode.");
    }

    public void snapCar(Car car) {
        System.out.println("Snapping car");
    }

    @Override
    public void snap(int exposure, double aperture) {
        System.out.printf("SNAP with exposure %d aperture %.2f\n", exposure, aperture);

    }
}
