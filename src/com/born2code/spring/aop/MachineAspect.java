package com.born2code.spring.aop;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.DeclareParents;
import org.springframework.stereotype.Component;

@Aspect
@Component
public class MachineAspect {

    @DeclareParents(value = "com.born2code.spring.aop.*", defaultImpl = com.born2code.spring.aop.Machine.class)
    private IMachine machine;

    /* Sample PCD PointCut Designation: within, this, execute, target, args */
    @Around("within(com.born2code.spring.aop.*)")
    public void runMachine(ProceedingJoinPoint proceedingJoinPoint) {
        System.out.println("*********** RUNNING *********");
        try {
            proceedingJoinPoint.proceed();
        } catch (Throwable e) {
            e.printStackTrace();
        }
        System.out.println("*********** Completed *********");
    }


}
