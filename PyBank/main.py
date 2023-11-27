{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "f0d220d9",
   "metadata": {},
   "outputs": [],
   "source": [
    "#import dependencies\n",
    "import os\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b48752e9",
   "metadata": {},
   "outputs": [],
   "source": [
    "#INSTRUCTIONS\n",
    "#The total number of months included in the dataset\n",
    "#The net total amount of \"Profit/Losses\" over the entire period\n",
    "#The changes in \"Profit/Losses\" over the entire period, and then the average of those changes\n",
    "#The greatest increase in profits (date and amount) over the entire period\n",
    "#The greatest decrease in profits (date and amount) over the entire period\n",
    "#Your analysis should align with the following results:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "3aa8c9a6",
   "metadata": {},
   "outputs": [],
   "source": [
    "#declare variables/lists\n",
    "total_months = 0\n",
    "amount = 0\n",
    "net_amount = 0\n",
    "changes_profit = 0\n",
    "total_profit = 0\n",
    "avg_changes = 0\n",
    "greatest_increase = 0\n",
    "greatest_decrease = 0\n",
    "\n",
    "profit_losses=[] #creating a list to store profit/losses\n",
    "date = []\n",
    "monthly_profit = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "62d17d91",
   "metadata": {},
   "outputs": [],
   "source": [
    "#read csv file\n",
    "budget_data = os.path.join(\"Resources\", \"budget_data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "7abc59d5",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open (budget_data) as csvfile: #need to read the csv file\n",
    "    csvreader = csv.reader(csvfile, delimiter = ',')\n",
    "    #print(csvreader) needed to test functionality\n",
    "    csv_header = next(csvreader)\n",
    "    #print(f\"CSV Header: {csv_header}\") #needed to test functionality\n",
    "    \n",
    "    for row in csvreader:\n",
    "        #print(row) #just wanted to verify that the entire data set was being read\n",
    "        \n",
    "        #The total number of months included in the dataset\n",
    "        total_months = total_months + 1\n",
    "        date.append(row[0])\n",
    "        \n",
    "        #The net total amount of \"Profit/Losses\" over the entire period\n",
    "        profit_losses.append(row[1])\n",
    "        net_amount += int(row[1])\n",
    "        \n",
    "        #The changes in \"Profit/Losses\" over the entire period, and then the average of those changes\n",
    "        amount = int(row[1])\n",
    "        profit_change = amount - changes_profit\n",
    "        monthly_profit.append(profit_change)\n",
    "        \n",
    "        total_profit += profit_change\n",
    "        \n",
    "        avg_changes = (total_profit/total_months)\n",
    "        \n",
    "        #The greatest increase in profits (date and amount) over the entire period\n",
    "        greatest_increase = max(profit_losses)\n",
    "        \n",
    "        #The greatest decrease in profits (date and amount) over the entire period\n",
    "        greatest_decrease = min(profit_losses)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "1c4ccb18",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Financial Analysis\n",
      "----------------------------\n",
      "Total Months:86\n",
      "Total:22564198\n",
      "Average Change:262374.3953488372\n",
      "Greatest Increase in Profits:99841\n",
      "Greatest Decrease in Profits:-1066544\n"
     ]
    }
   ],
   "source": [
    "#Your analysis should align with the following results:\n",
    "print(\"Financial Analysis\")\n",
    "print(\"----------------------------\")\n",
    "print(\"Total Months:\" + str(total_months))\n",
    "print(\"Total:\" + str(net_amount))\n",
    "print(\"Average Change:\" + str(avg_changes))\n",
    "print(\"Greatest Increase in Profits:\" + str(greatest_increase) +str)\n",
    "print(\"Greatest Decrease in Profits:\" + str(greatest_decrease))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "595f8ec0",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
