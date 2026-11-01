// Teaching contexts are re-denominated in TWD; no exchange-rate conversion occurs.
export function taiwanCurrency(text){
 return text.replaceAll('£','NT$').replaceAll('GBP','TWD').replaceAll('gbp','twd')
  .replace(/_pounds?\b/g,'_twd').replace(/\bpounds?\b/g,'TWD')
  .replaceAll('英鎊','新臺幣').replaceAll('en-GB','zh-TW')
  .replace(/NT\$(\d{4,})(\.\d+)?/g,(_,n,d='')=>'NT$'+Number(n).toLocaleString('zh-TW')+d);
}
