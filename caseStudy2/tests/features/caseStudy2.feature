Feature: Send box to the delivery point
  As a operator,
  I want to send the box to the delivery point using the robot
  So that I can automate the process

  Scenario: Move box from A to B
    Given the robot setup is initialized
    And the conveyor setup is initialized
    And the robot is at home
    And the box is in the point A
    When the pickAndPlace finish
    Then the box should be in the position B




