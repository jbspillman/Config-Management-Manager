# Config-Management-Manager

Trying to create a configuration manager type of thing. </br>

<hr>

1. #### Global Policies for All Platforms
   * Apply to everything, unless setting applied at lower level.
     </br>
2. #### Regional Policies (_Geographic or Other Special Requirements_).
   * NAMR, EMEA, APAC, SPECIAL
     </br>   
3. #### Site based Policies (_Geographic or Other Special Requirements_).
   * Data Center, Small Site, etc.
     </br>
4. #### Environment Designation Policies.
   * PRD, UAT, TST, LAB, SPECIAL
     </br>
5. #### Use Case or Work Load Policies.
   * Application, User, Worm, Archive, Special
     </br>
6. #### Product Specific Policies (_diverge at this point_).
   * Product A, Product B, Product C
     </br>
7. #### RBAC (_Product Roll Based Access Controls_).
   * Security is largely based on Product, Use Case, Environment, etc.
     </br>
8. #### Cluster Configuration Rules
   * Cluster specific settings based on Product, etc.
     </br>
9. #### Namespace Configuration Rules
   * Namespace specific settings based on Cluster, Use Case, Env, etc.
     </br>
10. #### Storage Path Configuration Rules
    * Volume or Path specific settings.
      </br>

<hr>

