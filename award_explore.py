import pandas as pd
import numpy as np

data = []

f = range(1,75,1)
for n in f:
    print(n)
    in_file = open('/Users/annethessen/NSF_awards/award_data/' + str(n) + '.txt', 'r')
    next(in_file)
    for line in in_file:
        line.strip('\n')
        row = line.split('\t')
        #print(row[0:24])
        data.append(row[0:24])
arr = np.array(data) #dtype=['U7','U150','U25','U50','M8','M8','U25','U25','U25','U25','U25','M8','f8','U25','U25','U25','U25','U25','U25','U25','U25','U25','U25','f8','U500'])
labels = ['AwardNumber','Title','NSFOrganization','Program(s)','StartDate','LastAmendmentDate','PrincipalInvestigator','State','Organization','AwardInstrument','ProgramManager','EndDate','AwardedAmountToDate','Co-PIName(s)','PIEmailAddress','OrganizationStreet','OrganizationCity','OrganizationState','OrganizationZip','OrganizationPhone','NSFDirectorate','ProgramElementCode(s)','ProgramReferenceCode(s)','ARRAAmount','Abstract']
df = pd.DataFrame(arr, columns=labels, index=['AwardNumber'])
print('complete')