# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ/.,1234567890\t\n')
myStr = '''
Rishabh Garikiparithi
rishabh.garikiparithi@mail.utoronto.ca
linkedin.com/in/rishabh-g/
rishabhgarikiparithi.wix.com/portfolio
github.com/rishyfishy

Experience

Hyperloop Braking Subsystem              October 2019 to January 2020
Lead Mechanical Designer
 - Developed pneumatic braking system from scratch for SpaceX Competition.
 - Taught all new members how to use SolidWorks at the CSWA Level.
 - Designed components for energy and structures subsystems.

Human Powered Vehicle Design Team        April 2020 to January 2020 
Sponsorship Director 
 - Expanded the team’s sponsor network to acquire valuable resources.
 - Helped get over $10,000 in sponsorships for the team.
 - Spearheaded 4 workshops on advanced tools in SolidWorks and 			     workflow optimization tips to improve CAD speed by over 300%

Microcellular Plastics Manufacturing Lab       May 2020 to August 2020
Research Assistant
 - Created PVDF samples using compression molding and batch foaming.
 - Analyzed material samples using DSC and other technologies. 
 - Wrote a 10,000-word paper on BN nanocomposites with 160 references.

Human Powered Vehicle Design Team           September 2019 to April 2020
Lead Structural Designer
 - Designed vehicle frame for ASME Challenge and world speed record.
 - Used advanced surface modeling and FEA to double the safety factor.
 - Got hands-on experience with machining and carbon fiber layups. 


Projects
Traffic Sign Recognition 
Designed a convolutional neural network using Pytorch to recognize German traffic signs in a variety of lighting conditions. Optimized model hyperparameters, achieving a test accuracy of 97% 

CPU Transient Thermal Simulation
Simulated heat transfer through CPU IHS with and without an external heat-sink in SolidWorks. Compared results to show the importance of good thermal management. 

CNC Machine
Designed a CNC mill from scratch using Solidworks.	Reduced costs by 40% through design iteration and conducting part selection, considering manufacturability and cost effectiveness. Link to report

Injection Moldable Drawer Guides
Modeled and 3D printed replacement drawer hardware, optimized with topology optimization, reducing weight by about 50%. Now my mom’s drawers are fixed. As a design study, I modified the part for injection molding and made molds.

CAD Skills
 SolidWorks (CSWP Certified) 
 - FEA Static and Thermal Simulations
 - Mold Design
 - Advanced Surface Modeling
 AutoCAD, Autodesk Inventor 
 NX (Core Designer)
 ANSYS Workbench

Other Skills
 Oral Communication and Presentation
 Technical and Non-technical Writing
 Quick and Enthusiastic Learner
 Passion for Innovative Technology


'''
answer = ''.join(filter(whitelist.__contains__, myStr))


# %%
print (answer)


# %%
f = open("resume.txt", "a")
f.write(answer)
f.close()


# %%
class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next
  def __str__(self):
    current_node = self
    result = []
    while current_node:
      result.append(current_node.val)
      current_node = current_node.next
    return str(result)

def remove_kth_from_linked_list(head, k):
    mynode=head
    for i in range(k-1):
        mynode=mynode.next
    mynode.next=mynode.next.next 

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(head)
# [1, 2, 3, 4, 5]
remove_kth_from_linked_list(head, 3)
print(head)
# [1, 2, 4, 5]


# %%



