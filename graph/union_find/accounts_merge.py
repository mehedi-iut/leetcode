from collections import defaultdict
accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

class Solution:
	def accountMerge(self, accounts):
		parent = [i for i in range(len(accounts))]
		rank = [1]*len(accounts)

		def find(n):
			p = parent[n]
			while p != parent[p]:
				parent[p] = parent[parent[p]]
				p = parent[p]
			return p

		def union(n1, n2):
			p1, p2 = find(n1), find(n2)
			if p1 == p2:
				return

			if rank[p1]>rank[p2]:
				parent[p2] = p1
				rank[p1] += rank[p2]
			else:
				parent[p1] = p2
				rank[p2] += rank[p1]
		
		accountsCount = len(accounts)
		email2AccountIdx = {}
		# create { "email": 0 } hash map
		for i in range(accountsCount):
			account = accounts[i]
			for j in range(1, len(account)):
				email = account[j]
				# email not in the hashmap, add to the hashmap
				if email not in email2AccountIdx:
					email2AccountIdx[email] = i
				# if email already present in the hashmap,
				# we change the latest email parent i.e id to the previous same email id
				# using union function
				else:
					union(i, email2AccountIdx[email])
		# in components, we map id to emails
		# as we set same email to same id by changing the parent of the same email to one id
		components = defaultdict(list)
		for email, group in email2AccountIdx.items():
			# when we add email to compnents hashmap, we find the parent of the email
			# as same email has same parent, we can group the email together
			components[find(group)].append(email)
		# now we will merge the accounts with name
		merged_accounts = []
		for group, emails in components.items():
			name = accounts[group][0]
			merged_accounts.append([name] + sorted(emails))

		return merged_accounts

sln = Solution()
print(sln.accountMerge(accounts))

