#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/inet.h>
#include <linux/netfilter.h>
#include <linux/netfilter_ipv4.h>
#include <linux/ip.h>
#include <linux/tcp.h>

static struct nf_hook_ops filter;

unsigned int filterFunc(void *priv, struct sk_buff *skb,
                 const struct nf_hook_state *state)
{
  struct iphdr *iph;
  struct tcphdr *tcph;

  iph = ip_hdr(skb);
  tcph = (void *)iph+iph->ihl*4;

  // Preventing VM A (10.0.2.4) from doing telnet to others
  if (iph->protocol == 6 &&                 //TCP protocol
      tcph->dest == htons(23) &&            //dest_port
      iph->saddr == in_aton("10.0.2.4")     //src_ip
      )
      {
          return NF_DROP;
      }
      else
      {
          return NF_ACCEPT;
      }

  // Preventing VM A (10.0.2.4) from visiting a website (www.facebook.com)
  if (iph->saddr == in_aton("10.0.2.4") &&      //src_ip
      iph->daddr == in_aton("157.240.13.35")    //dest_ip
      )
      {
          return NF_DROP;
      }
      else
      {
          return NF_ACCEPT;
      }
}

int setUpFilter(void) {
        printk(KERN_INFO "Registering a filter.\n");
        filter.hook = filterFunc; 
        filter.hooknum = NF_INET_POST_ROUTING;
        filter.pf = PF_INET;
        filter.priority = NF_IP_PRI_FIRST;

        // Register the hook.
        nf_register_hook(&filter);
        return 0;
}

void removeFilter(void) {
        printk(KERN_INFO "Filter is being removed.\n");
        nf_unregister_hook(&filter);
}

module_init(setUpFilter);
module_exit(removeFilter);

MODULE_LICENSE("GPL");